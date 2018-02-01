#import modules 
import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import xlrd
import xlwt
from xlutils.copy import copy

#check for the type of Platform
if platform.system() == 'Windows':
    PHANTOMJS_PATH = 'D:\\ProgramFiles\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
else:
    PHANTOMJS_PATH = 'D:\\ProgramFiles\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
#OutPutFilePath="E:\\IA_Work\\webscraping\\output\\CnetUserReviews.xls"
#Product link page scraper function
def articleScraper(ProductLink):
	browser = webdriver.PhantomJS(PHANTOMJS_PATH)
	browser.get(ProductLink)
	soup = BeautifulSoup(browser.page_source, "lxml")
	prducttxt=soup.find("div",{"id":"modelInfo"})
	prdct= prducttxt.prettify()
	pname=prducttxt.h3.string
	pNumber=prducttxt.find("span" , "partNumber").string
	productNumber= pNumber[13:]
	print pname
	print "--------"
	print productNumber
	print "--------"
	article_List=soup.findAll('article',{"class":"fyre-comment-article fyre-comment-source-0"})
	for article in article_List:
		print "inside for"
		ContentPros=""
		ContentCons=""
		ContentSummary=""
		UserRating=""
		headerTxt=article.h3
		articleHeader=headerTxt.text
		articleCommentsTxt=article.find("div",{"class":"fyre-comment"})
		commentsPList=articleCommentsTxt.findAll("p")
		i=0
		s=0
		RatingText=article.find("div",{"class":"fyre-reviews-rating-wrapper"})
		RatingLableVal=RatingText.find("label")
		RatingStyle=RatingLableVal['style'][7:-1]
		UserRating=str(float(RatingStyle)/20)
		for comments in commentsPList:
			#comments.text
			if comments.has_attr('class'):
				strongTag=comments.find("strong").text
				if strongTag.lower()=='Pros'.lower():
					ContentPros=comments.text[4:]
				if strongTag.lower()=='Cons'.lower():
					ContentCons=comments.text[4:]
			#print comments.find("strong")
			if(comments.find("strong")):
				sTag=comments.find("strong").text
				if sTag.lower()=="Summary".lower():
					s=1
					ContentSummary=comments.text[7:]
			if s==1:
				ContentSummary=ContentSummary + comments.text+"\n"
		#print "workbook opening"
		rb = xlrd.open_workbook("E:\\IA_Work\\webscraping\\output\\CnetUserReviews.xls")
		r_sheet = rb.sheet_by_index(0) 
		r = r_sheet.nrows
		wb = copy(rb)
		sheet = wb.get_sheet(0)
		sheet.write(r,0,pname)
		sheet.write(r,1,productNumber)
		sheet.write(r,2,articleHeader)
		sheet.write(r,3,UserRating)
		sheet.write(r,4,ContentPros)
		sheet.write(r,5,ContentCons)
		sheet.write(r,6,ContentSummary)
		wb.save("E:\\IA_Work\\webscraping\\output\\CnetUserReviews.xls")
		print "file saved"
def main():
		plink="http://www.cnet.com/products/microsoft-surface-pro-4/user-reviews/"
		articleScraper(plink)

if __name__ == "__main__":
    main()