from datetime import datetime

def dynamic_content():
    return "You could have this function return anything you want :0"

print('''\
<html>
<body>
<h1>Test Header</h1>
<p>Generated {0}</p>
<p>{1}</p>
</body>
</html>'''.format(datetime.now(), dynamic_content()))
