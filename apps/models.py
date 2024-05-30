from django.db import models

from treenode.models import TreeNodeModel

class Root(TreeNodeModel):
    treenode_display_name = "name"
    name = models.CharField(max_length=30)

    class Meta(TreeNodeModel.Meta):
        verbose_name = "Category"
        verbose_name_plural = "Categories"