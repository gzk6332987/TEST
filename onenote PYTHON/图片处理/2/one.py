from PIL import Image,ImageColor
pic = Image.open('p.jpg')
x,y =pic.size
print(x,y)
if x*y > 100000000:
    print(f"这可能是一亿像素图片,为{x*y}")
pic.thumbnail((x//2,y//2))
pic.save('vai.jpg')