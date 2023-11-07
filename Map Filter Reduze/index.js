document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('getMessage').onclick = function(){
      const req = new XMLHttpRequest();
      req.open("GET",'json/cats.json',true);
      req.send();
      req.onload = function(){
        const json = JSON.parse(req.responseText);
        let html = "";
        // Adicione o código abaixo desta linha
        json.forEach(function(val) {
          const keys = Object.keys(val);
          html += "<div class='cat'>;";
          keys.forEach(function(keys) {
            html += "<strong>" + key + "</strong>" + val[key] + "<br>";
          });
           html += "</div><br>";
        });
        // Adicione o código acima desta linha
        document.getElementsByClassName('message')[0].innerHTML = html;
      };
    };
});