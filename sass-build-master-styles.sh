source_dir='source/_static/sass'
dest_dir='source/_static'

sass --update $source_dir:$dest_dir --style compressed --trace
