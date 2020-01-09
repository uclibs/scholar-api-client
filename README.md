# Usage

Set server root and API key in `config.ini`.

```python
from work import Update


u = Update({"id": "foo1234", "work_type": "articles", "title": "My title"})
# r is a requests object
r = u.update()
```