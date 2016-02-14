
  chmod +x hello.py
  wget https://pypi.python.org/packages/source/p/pymongo/pymongo-3.2.1.tar.gz#md5=1894865cc436fbea833b9228dc479db7
  tar -xzf pymongo-3.2.1.tar.gz 
  rm pymongo-3.2.1.tar.gz 
  cd pymongo-3.2.1/
  python setup.py build
