


import markdown
import glob
import os



def MakeHTMLFromMD(mdFilename, templateFilename, outputFilename):
    """
    """
    html        = markdown.markdown(open(mdFilename,'r').read())
    template    = open(templateFilename).read()
    open(outputFilename,'w').write(template%html)


def MakeHTMLFromTHTML(thFilename, templateFilename, outputFilename):
    """
    """
    html        = open(thFilename,'r').read()
    template    = open(templateFilename).read()
    open(outputFilename,'w').write(template%html)




mdFilenames = glob.glob('Pages/*.md')
for mdFilename in mdFilenames:
    base =  os.path.basename( os.path.splitext(mdFilename)[0] )
    outputFileName = base+'.html'
    try:
        templateFileName = glob.glob('Templates/'+outputFileName)[0]
    except IndexError:
        templateFileName = 'Templates/DefaultTemplate.html'
    print('MD[%s+%s -> %s]'%(base, templateFileName, outputFileName))
    MakeHTMLFromMD(mdFilename, templateFileName, outputFileName)


thFilenames = glob.glob('Pages/*.thtml')
for thFilename in thFilenames:
    base =  os.path.basename( os.path.splitext(thFilename)[0] )
    outputFileName = base+'.html'
    templateFileName = glob.glob('Templates/'+outputFileName)
    try:
        templateFileName = glob.glob('Templates/'+outputFileName)[0]
    except IndexError:
        templateFileName = 'Templates/DefaultTemplate.html'
    print('THTML[%s+%s -> %s]'%(base, templateFileName, outputFileName))
    MakeHTMLFromTHTML(thFilename, templateFileName, outputFileName)




