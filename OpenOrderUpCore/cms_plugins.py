from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from OpenOrderUpCore.models import *

class CMSOrderPlugin(CMSPluginBase):
    model = OrderPlugin
    name = _("Orders Up")
    render_template = "orders_up.html"

    def render(self, context, instance, placeholder):
        context.update({
            'restaurant':instance.restaurant,
            'object':instance,
            'placeholder':placeholder 
        })
        return context

plugin_pool.register_plugin(CMSOrderPlugin)


class CMSThemeFooterPlugin(CMSPluginBase):
    model = ThemeFooterPlugin
    name = _("Order Up - Bottom")
    render_template = "footer.html"

    def render(self, context, instance, placeholder):
        context.update({
            'theme':instance.theme,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSThemeFooterPlugin)

class CMSThemeHeaderPlugin(CMSPluginBase):
    model = ThemeHeaderPlugin
    name = _("Order Up - Top")
    render_template = "header.html"

    def render(self, context, instance, placeholder):
        context.update({
            'theme':instance.theme,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSThemeHeaderPlugin)

class CMSThemeLeftPlugin(CMSPluginBase):
    model = ThemeLeftPlugin
    name = _("Order Up - Left")
    render_template = "left.html"

    def render(self, context, instance, placeholder):
        context.update({
            'theme':instance.theme,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSThemeLeftPlugin)

class CMSThemeRightPlugin(CMSPluginBase):
    model = ThemeRightPlugin
    name = _("Order Up - Right")
    render_template = "right.html"

    def render(self, context, instance, placeholder):
        context.update({
            'theme':instance.theme,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSThemeRightPlugin)

