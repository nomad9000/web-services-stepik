from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'qa.views.mainpage'),
    url(r'^login/$', 'qa.views.loginpage'),
    url(r'^signup/.*', 'qa.views.signuppage'),
    url(r'^question/(?P<questionid>\d+)/$', 'qa.views.questionpage', name='questionid'),
    url(r'^ask/.*', 'qa.views.askpage'),
    url(r'^popular/.*', 'qa.views.popularpage'),
    url(r'^new/.*', 'qa.views.test'),
    url(r'^answer/.*', 'qa.views.answerpage'),
)
