import glob

f = open("index.html", "w")
f.write("""
<html>
  <head>
    <style>
      img {
      height: 200px;
      width: auto;
      }
    </style>
  </head>
  <body>
""")

for filename in glob.iglob('./*.JPG'):
         f.write('<img src="%s" /><br>\n' % filename)

f.write("""
</body>
</html>
""")
