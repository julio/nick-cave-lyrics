var LyricsApp = window.LyricsApp || {};

(function scopeWrapper($) {

    var apiEndpoint = LyricsApp.apiEndpoint;

    LyricsApp.populateAlbums = function () {
        $.get(apiEndpoint + '/albums').done(function (data) {
            data.forEach(function (album) {
                $('TBODY').append('<tr><td><a href="album.html#' + album.id + '">'+ album.title +'</a></td></tr>');
            });
            $('TBODY').append('<tr><td></td></tr>');
        });
    };

    LyricsApp.loadAlbum = function () {
        $.get(apiEndpoint + '/albums/' + location.hash.substring(1)).done(function (album) {
            var albumPanel = $('<div class="panel">');
            albumPanel.addClass('panel-info');
            albumPanel.append('<div><img src="'+ album.cover + '"/></div>');
            $('#album').append(albumPanel);

            album.songs.forEach(function (song) {
                var panel = $('<div class="panel">');
                panel.addClass('panel-info');
                panel.append('<div class="panel-heading">' + song.title + '</div>');

                var body = $('<div class="panel-body">');
                song.lyrics.forEach(function (verse) {
                    var p = $('<p>' + verse + '</p>');
                    body.append(p);
                });

                panel.append(body);

                var row = $('<div class="row">');
                var buffer = $('<div class="col-xs-4">');
                var holder = $('<div class="col-xs-8">');
                holder.append(panel);

                row.append(holder);
                row.append(buffer);

                $('#album').append(row);
            });
            window.scrollTo(0, document.body.scrollHeight);
        });
    };

}(jQuery));