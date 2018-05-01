builder='html'
srcdir='source'
destdir='build/html'

rm -rf $destdir &&\
    sphinx-build -b $builder $srcdir $destdir
