from datetime import datetime

print('''\
<html>
<body>
<h1>Test Header</h1>
<p>Generated {0}</p>
</body>
</html>'''.format(datetime.now()))
