from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin
from .models import *
from treenode.forms import TreeNodeForm

class RootAdmin(TreeNodeModelAdmin):
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION

    form = TreeNodeForm

admin.site.register(Root,RootAdmin)