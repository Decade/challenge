# Apache Combined Log Format parser
Uses Node.js or io.js. Takes a log file with `Apache Combined Log Format <https://httpd.apache.org/docs/2.2/logs.html#combined>` log entries and spits out JSON.

Typical use would be:
`node parser.js < access.log > access.json`

Or you could do silliness like:
```
echo #!/usr/bin/node > parser
cat parser.js >> parser
chmod +x parser
```
And then use it like a normal command-line program.