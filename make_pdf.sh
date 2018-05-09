sphinx-build -b latex source build/latex &&\
    pushd build/latex &&\
    make &&\
    popd
