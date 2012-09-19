from pyramid.view import view_config

from .models import (
    DBSession,
    User,
    )

@view_config(route_name='home', renderer="pyramid_blogr:templates/index.mako")
def index_page(request):
    return {}

@view_config(route_name='blog', renderer="pyramid_blogr:templates/view_blog.mako")
def blog_view(request):
    return {}

@view_config(route_name='blog_action', match_param="action=create", request_method="POST",
             renderer="pyramid_blogr:templates/edit_blog.mako")
@view_config(route_name='blog_action', match_param="action=edit", request_method="POST",
             renderer="pyramid_blogr:templates/edit_blog.mako")
def blog_create_update(request):
    return {}

@view_config(route_name='sign_in', renderer="string", request_method="POST")
def sign_in(request):
    return {}

@view_config(route_name='sign_out', renderer="string")
def sign_out(request):
    return {}