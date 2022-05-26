from unittest import TestCase, mock

from source_code.domain.test.fixtures.PlaylistsFixtures import playlists
from source_code.infrastructure.app import app
from source_code.infrastructure.main.controllers import PlaylistController


class TestPlaylistController(TestCase):
    def test_list_playlist_response_with_the_expected_html(self):
        with mock.patch.object(PlaylistController, 'list_user_playlist_items', new=playlists):
            response = app.test_client().get('/list')
            self.assertEqual(response.data.decode("utf-8").replace("\n", "").replace(" ", ""),
                             expected_response()
                             )


def expected_response() -> str:
    return """<!DOCTYPE><htmllang="ES"><head><title>Toolify</title><linkrel='shortcuticon'type='image/x-icon'href="/static/toolify.png"/><linkhref="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"rel="stylesheet"integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"crossorigin="anonymous"></head><body><navclass="navbarnavbar-lightbg-lightshadow-smmb-5"><imgsrc="/static/images/toolify.png"class="mx-autod-block"alt=""></nav><divclass="container"><divclass="row"><divclass="colp-1"><divclass="card"style="width:18rem;"><imgsrc='Asimpleuri'class="card-img-top"height="286px"width="286px"alt="..."><divclass="card-body"><h5class="card-title">PLAYLIST_NAME</h5><pclass="card-text">Asimpledescription</p></div><ulclass="list-grouplist-group-flush"><liclass="list-group-item"><strong>Totaltracks:</strong>10</li></ul><divclass="card-body"><buttontype="button"id='PLAYLIST_ID'class="btnbtn-primaryreorder">Orderbyreleasedate(desc)</button></div></div></div></div></div><scriptsrc="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"crossorigin="anonymous"></script><script>varreorderButton=document.getElementsByClassName('reorder');for(leti=0;i<reorderButton.length;i++){reorderButton[i].addEventListener('click',function(){varhttp=newXMLHttpRequest();varurl='http://localhost/order'varparams='playlist='+reorderButton[i].id;http.open('POST',url,true);http.setRequestHeader('Content-type','application/x-www-form-urlencoded');http.onreadystatechange=function(){if(http.readyState===4&&http.status===200){alert("PLAYLISTWASORDERED");}}http.send(params);});}</script></body></html>"""
