from jinja2 import BaseLoader, Environment
from jinja2.exceptions import TemplateNotFound

import os


class CustLoader(BaseLoader):
    def __init__(self, searchpath: str, prefix_allow: Optional[str] = None) -> None:
        """
        Args:
            searchpath ([str]): base directory that `template` is relative to
            prefix_allow ([str], optional): if provided, only allow `template`s matching the
            provided prefix
        """
        self.prefix_allowlist = prefix_allow
        self.searchpath = searchpath
        super().__init__()

    def get_source(
            self, environment: Environment, template: str
    ) -> Tuple[str, str, Optional[Callable[[], bool]]]:
        """Superclass override (https://jinja.palletsprojects.com/en/3.0.x/api/#loaders)
        When told to find a template with name `foo.html.jinja2`, will attempt to find a template
        with name `foo.md` and wrangle it into Jinja format.
        Raises:
            TemplateNotFound: [description]
        Returns:
            Tuple[str,str,Optional[Callable[[],bool]]]: (source, filename, is_uptodate);
                `source` is the Jinja template source,
                `filename` is the path to the file that Jinja can use for stack
                traces,
                `is_uptodate` (if provided) is used for template reloading; if
                it returns `False` then the template is reloaded.
        """

        template = template.replace("/", os.sep)
        # `template` (as given in arguments) is a Jinja path (/ on all paths)
        # from hereon we can assume it is an OS-compatible path.
        return (source, filename, None)
