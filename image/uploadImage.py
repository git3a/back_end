from django.views.decorators.http import require_http_methods
import filetype, hashlib
from image.views import returnOk, returnForbidden, returnBadRequest
from image.models import UploadImage
from django.conf import settings

# 上传文件的视图
@require_http_methods(["POST"])
def uploadImage(request):
	# 从请求表单中获取文件对象
	file = request.FILES.get("file", None)
	if not file:  # 文件对象不存在， 返回400请求错误
		return returnBadRequest("need file.")
	
	# 计算文件md5
	md5 = pCalculateMd5(file)
	uploadImg = UploadImage.getImageByMd5(md5)
	if uploadImg:   # 图片文件已存在， 直接返回
		return returnOk({'url': uploadImg.getImageUrl()})
	
	# 获取扩展类型 并 判断
	ext = pGetFileExtension(file)
	if not pIsAllowedImageType(ext):
		return returnForbidden("文件类型错误")
	
	# 检测通过 创建新的image对象
	# 文件对象即上一小节的UploadImage模型
	uploadImg = UploadImage(filename = file.name, file_md5 = md5, file_type = ext, file_size = file.size)
	#uploadImg.filename = file.name
	#uploadImg.file_size = file.size
	#uploadImg.file_md5 = md5
	#uploadImg.file_type = ext
	uploadImg.save()  # 插入数据库
	
	# 保存 文件到磁盘
	with open(uploadImg.getImagePath(), "wb+") as f:
		# 分块写入
		for chunk in file.chunks():
			f.write(chunk)
	
	
	# 返回图片的url以供访问
	return returnOk({"url": uploadImg.getImageUrl()})


# 检测文件类型
# 我们使用第三方的库filetype进行检测，而不是通过文件名进行判断
# pip install filetype 即可安装该库
def pGetFileExtension(file):
	rawData = bytearray()
	for c in file.chunks():
		rawData += c
	try:
		ext = filetype.guess_extension(rawData)
		return ext
	except Exception as e:
		# todo log
		return None

# 计算文件的md5
def pCalculateMd5(file):
	md5Obj = hashlib.md5()
	for chunk in file.chunks():
		md5Obj.update(chunk)
	return md5Obj.hexdigest()

# 文件类型过滤 我们只允许上传常用的图片文件
def pIsAllowedImageType(ext):
	if ext in ["png", "jpeg", "jpg"]:
		return True
	return False

