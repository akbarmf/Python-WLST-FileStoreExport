from java.io import FileInputStream


def exportFileStores(file):

    cd('/')
    #redirect('/dev/null','false')
    filestores = cmo.getFileStores()

    for fs in filestores:
      fsName = fs.getName()
      fsDirectory = fs.getDirectory()
      fsTarget = fs.getTargets()
      serverTarget = ''
	  
      for target in fsTarget:
        serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

      print('# exporting filestore: ' + fsName )
      print('# exporting directory: ' + str(fsDirectory) )
      print('# exporting target: ' + str(serverTarget) )
      print('\n')
	  
      if str(fsDirectory) == 'None':
        fsDirectory = ''
      elif str(serverTarget) == 'None':
        serverTarget = ''
	  
      exp = 'filestore,' + str(fsName) + ',' + str(fsDirectory) + ',' + str(serverTarget) +'\n'
      file.write(exp)

def main():
    propInputStream = FileInputStream(sys.argv[1])
    configProps = Properties()
    configProps.load(propInputStream)

    url=configProps.get("adminUrl")
    username = configProps.get("importUser")
    password = configProps.get("importPassword")
    csvLoc = configProps.get("csvLoc")

    connect(username,password,url)
	
    print('======= Export FileStore =======\n')	
	
    file=open(csvLoc, 'a+')
	
    exportFileStores(file)
            
    print('------- End of Export FileStore -------\n')
    disconnect()

main()
