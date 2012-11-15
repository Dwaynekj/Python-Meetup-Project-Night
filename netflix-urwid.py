import netflix, urwid

api = netflix.NetflixAPI(api_key="bfddvnduhs3xxyhxpf5x9sue", api_secret="7BZZdYt4GS")


def exit():
    if key in ('q'):
        raise urwid.ExitMainLoop()

def results(answer):
    query = api.get("catalog/titles/autocomplete", {"term" : answer})
    for title_info in query["autocomplete"]["autocomplete_item"]:
        yield title_info["title"]["short"]

palette = [('I say', 'default,bold', 'default', 'bold'),]
ask = urwid.Edit(('I say', u"What movie are you looking for?\n"))
reply = urwid.Text(u"")
button = urwid.Button(u'Exit')
div = urwid.Divider()
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Filler(pile, valign='top')

def on_ask_change(edit, new_edit_text):
    a = []
    if len(new_edit_text) < 3:
        reply.set_text(('I say', u"Enter at least 3 characters"))
        return
    query = results(new_edit_text)
    for i in query:
        a.append(i)
    reply.set_text(('I say', u"Nelfix found: %s" % a))

def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)
urwid.MainLoop(top, palette).run()
