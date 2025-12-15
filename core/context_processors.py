def active_page(request):
    return {
        "current_url_name": request.resolver_match.url_name
    }
