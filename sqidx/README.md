# pmccabe


# Cmetrics
## halstead <file>

``` bash
sed -n "$(start_line), $(end_line)p" $(file_name) > $(tmp_file)
halstead $(tmp_file)
```
