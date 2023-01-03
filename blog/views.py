from django.shortcuts import render
from .models import Post, Attachment, Contact, Tag
from django.db.models import Q
import ipdb
from django.core.paginator import Paginator
from .models import HTMLForm


# template body: https://blog01.superservidor.info/
# https://blog.wedologos.com.br/exemplos-de-blogs/
def description_replace():
    return



def main(request):
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    first_pub = Post.objects.order_by('-publiched_date').first()
    all_pub = pub.exclude(id=first_pub.id)
    tags = Tag.objects.all()    



    #PAGINAÇÃO
    paginator = Paginator(pub, 3) 
    page = request.GET.get('page')
    page_pub = paginator.get_page(page)



    #ipdb.set_trace()
    atts = Attachment.objects.order_by('-id')[:10]

    contacts = Contact.objects.all()

    context = {
        'page':page,
        'page_pub':page_pub,
        'posts': pub,
        'first_pub': first_pub,
        'attachments': atts,
        'contacts': contacts,
        'tags': tags

    }

    return render(request, 'index.html', context)

def article(request, URLTitle):
    #ipdb.set_trace()
    URLT = URLTitle.replace('-',' ')
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    first_pub = Post.objects.order_by('-publiched_date').first()
    all_pub = pub.exclude(id=first_pub.id)
    atts = Attachment.objects.order_by('-id')[:10]
    article = Post.objects.get(title=URLT) #get object or 404
    contacts = Contact.objects.all()
    tags = Tag.objects.all()    


    context = {
        'article': article,
        'posts': all_pub,
        'first_pub': first_pub,
        'attachments': atts,
        'contacts': contacts,
        'tags': tags

    }
    return render(request, 'article.html', context)

def search(request):
    # filterSearchField = search_field.replace('-',' ')
    search_field = request.GET.get('search_field')
    if search_field == '':
        search_field = True
    tags = Tag.objects.all()    
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    first_pub = Post.objects.order_by('-publiched_date').first()
    all_pub = pub.exclude(id=first_pub.id)

    relatedPosts = Post.objects.filter(Q(title__icontains=search_field) | Q(main_tag__name__icontains=search_field) ,active=True).order_by('-publiched_date') #get object or 404

    #ipdb.set_trace()
    atts = Attachment.objects.order_by('-id')[:10]

    paginator = Paginator(relatedPosts, 5) 
    page = request.GET.get('page')
    relatedPosts = paginator.get_page(page)




    context = {
        'page': page,
        'relatedPosts': relatedPosts,
        'posts': pub,
        'first_pub': first_pub,
        'attachments': atts,
        'tags': tags
    }
    print(relatedPosts)
    print(page)
    
    return render(request, 'search.html', context)


def about(request):
    #ipdb.set_trace()
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    tags = Tag.objects.all()    
    form = HTMLForm

    context = {
        'authors':pub,
        'tags': tags,
        'form': form,

    }
    return render(request, 'about.html', context)

def contact(request):
    #ipdb.set_trace()
    pub = Post.objects.filter(active=True).order_by('-publiched_date')
    tags = Tag.objects.all()    

    context = {
        'authors':pub,
        'tags': tags

    }
    return render(request, 'contact.html', context)