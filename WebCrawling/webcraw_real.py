
import urllib.request
import os

urls ="""http://libertycity.org/wp-content/uploads/2018/03/iStock-640177838.jpg
http://dailyutahchronicle.com/wp-content/uploads/2017/10/professorrating.jpg
https://gazettereview.com/wp-content/uploads/2017/02/college-professor.jpg
https://researchdigest.files.wordpress.com/2018/03/gettyimages-481029389.jpg?w=845
https://www.fastweb.com/uploads/article_photo/photo/2036639/how-to-pick-the-best-professors.jpg
https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Toni_Morrison_2008-2.jpg/220px-Toni_Morrison_2008-2.jpg
https://sites.dartmouth.edu/jacko/files/2017/03/635972932911796323793121814_College-Professor.jpg
http://reflectorgsu.com/wp-content/uploads/2017/10/pro.jpg
https://www.chronicle.com//img/photos/biz/photo_85068_landscape_650x433.jpg
https://news.illinois.edu/files/6367/635343/131240.jpg
https://www.worldatlas.com/r/w728-h425-c728x425/upload/da/f0/cf/female-professor.jpg
http://thefederalist.com/wp-content/uploads/2015/11/shutterstock_330576656-998x666.jpg
https://researchers.anu.edu.au/researchers/white-hj/image
https://img-aws.ehowcdn.com/340x221p/photos.demandstudios.com/getty/article/178/209/87608538.jpg
https://cdn.noodle.com/media/articles/iStock_000062362416_XXXLarge.jpg.736x0_q85.jpg
http://admissionado.com/wp-content/uploads/2016/04/college_professors_blog_post.jpg
"""

urlList=urls.split('https')
urlList.pop(0)

#print(*urlList,sep="\n")
#print("=============================")


#https
for i in range(len(urlList)):
    urlList[i]="https"+urlList[i]

#print(*urlList,sep="\n")

outpath="C:/test/"

if not os.path.isdir(outpath):
    os.makedirs(outpath)


#jpg png
#img num
count=0
for i in range(len(urlList)):

    #fname,ext=os.path.splitext(urlList[i])
    if urlList[i].find(".jpg")!=-1:
        #ext==".jpg":
        print("in"+str(i))
        outfile="train"+str(count)+".jpg"
        try:
            urllib.request.urlretrieve(urlList[i], outpath+outfile)
            count+=1
        except Exception as e:
            print("shit!")
    elif urlList[i].find(".png")!=-1:
        #ext==".png":
        outfile ="train"+str(count)+".png"
        try:
            urllib.request.urlretrieve(urlList[i], outpath+outfile)
            count+=1
        except Exception as e:
            print("shit!")
    
    else:
        print("out"+str(i))
    

#outfile ="test.jpg"

