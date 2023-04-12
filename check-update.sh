#|/bin/bash
curl https://gitlab.com/Remmina/Remmina/-/tags  2>/dev/null | grep 'Release '|sed -e 's,.*<pre.*Release v,,;s,</pre>.*,,' | head -n1

