from wordcloud import WordCloud,ImageColorGenerator
import  matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
import jieba.analyse

content = open("我们.txt","rb").read()  #测试文本为网上中国有嘻哈的某篇博客文章
#tags extraction based on TF-IDF algorithm
tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
text =" ".join(tags)
print(text)
# text = unicode(text)

#读入背景图片
bj_pic=imread('t11.png')

#生成词云（通常字体路径均设置在C:\\Windows\\Fonts\\也可自行下载）
font=r'C:\Windows\Fonts\simhei.ttf'#不加这一句显示口字形乱码  ""报错 
wordcloud=WordCloud(mask=bj_pic,background_color='white',font_path=font,scale=3.5).generate(text)
  #img_color = ImageColorGenerator(self.img)
image_colors=ImageColorGenerator(bj_pic)
#显示词云

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('我们.jpg')
