
# urls will be a dictionary of url : path format
# all the resoures should be in pages folder!
# eg if the page for url "/contact/admin" is at "pages/contact/admin.html", give the following mapping: {"/contact/admin": "/contact/admin.html"}

DEFAULT_NOT_FOUND = "nf.html" # incase something goes wrong in mapping search!

urls = {"/" : "home.html",
        "/contact" : "contact.html"
        }
