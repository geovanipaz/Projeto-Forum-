from main.models import Post

def searchFunction(request):
    context={}
    posts = Post.objects.all()
    if 'search' in request.GET:
        query = request.GET.get('q')
        search_box = request.GET.get('search-box')
        if search_box == 'Descriptions':
            objects = posts.filter(content__icontains=query)
        else:
            objects = posts.filter(title__icontains=query)
        #filtro começa aqui    
        context = {
            'objects':objects,
            'query':query
        }
    return context