from PIL import Image, ImageEnhance

IM = Image.open('pic.png')
print(IM.size)
IM_size = IM.resize((10,10))

enh = ImageEnhance.Contrast(IM)
enh.enhance(5).show("30% 增强对比度")
IM.save('timg9.png')

IM_size.show()