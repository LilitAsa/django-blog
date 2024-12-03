def menu_context(request):
    return {
        "menu":  [
            {
                "link_title": "Home Page",
                "link_url_name": "index"
            },
            {
                "link_title": "About Site",
                "link_url_name": "about"
            },
            {
                "link_title": "Add Post",
                "link_url_name": "add_post"
            },
            {
                "link_title": "Contacts",
                "link_url_name": "contacts"
            },
            {
                "link_title": "Login",
                "link_url_name": "login"
            },
        ]
    }