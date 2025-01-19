def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == "Искать заметки по тегу" and tag:
        print(tag)
        notes_filtered = {} #тут будут заметки с выделенным тегом
        for note in notes:
            if tag in notes[note]["теги"]: 
                notes_filtered[note]=notes[note]
        button_tag_search.setText("Сбросить поиск")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == "Сбросить поиск":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Искать заметки по тегу")
        print(button_tag_search.text())
    else:
        pass
