

class Simplate(object):

    def __init__(self, template_string, title=None, defaults=""):
        self.template = Template(template_string, defaults)
        self.title = title.replace(" ", "") if title else "ImplementedTemplate"
        self.ImplementationClass = type(self.title, (Implementation, object), {})

    def implement(self):
        return self.ImplementationClass(self.template)


class Template(object):

    def __init__(self, template_string, defaults=""):
        self.template = template_string
        self.defaults = defaults
        self.arguments = {x[1]: self.defaults for x in template_string._formatter_parser() if x[1]}


class Implementation(object):

    TEMPLATE = ""

    def __init__(self, template_object):
        self.__class__.TEMPLATE = template_object.template
        for kwarg, kval in template_object.arguments.iteritems():
            setattr(self, kwarg, kval)

    def __str__(self):
        return self.__class__.TEMPLATE.format(**self.__dict__)