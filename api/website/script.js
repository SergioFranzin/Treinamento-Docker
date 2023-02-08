
function createTable(conteudo) {
    var tabela = document.createElement("table");
    var thead = document.createElement("thead");
    var tbody=document.createElement("tbody");
    var thd=function(i){return (i==0)?"th":"td";};
    for (var i=0;i<conteudo.length;i++) {
      var tr = document.createElement("tr");
      for(var o=0;o<conteudo[i].length;o++){
        var t = document.createElement(thd(i));
        var texto=document.createTextNode(conteudo[i][o]);
        t.appendChild(texto);
        tr.appendChild(t);
      }
      (i==0)?thead.appendChild(tr):tbody.appendChild(tr);
    }
    tabela.appendChild(thead);
    tabela.appendChild(tbody);
    return tabela;
  }

function main(){
    //let url = 'http://flask-container:9001/products' //acessando direto a porta do flask-container ao utilizar a tag --link
    //let url = 'http://172.17.0.3:9001/products' //acessando direto pelo IP do container flask-container
    let url = 'http://localhost:9001/products' //acessando a porta do meu local host, que por sua vez, acessa a porta do container flask-container
    let resp = new XMLHttpRequest()
    resp.open("GET", url, false)
    resp.send()  
    let response = JSON.parse(resp.responseText)
    var items = [['ID', 'Produto', 'Preço']] 
    response.forEach(item => {
        items.push([item['id'], item['name'], item['price']])
        
    });
    console.log(items)
    let table = document.getElementById('tabela').appendChild(createTable(items))
}

main()