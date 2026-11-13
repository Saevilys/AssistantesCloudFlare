// locate.js — Cross-section search: tells you where an assistant is
// Loads on every page, builds a name→section map, shows a hint when local search returns 0
(function(){
  var nameMap={};
  var loaded=false;

  function classify(a){
    if(a.collection==='roomservice'){return{section:'Service de Nuit',url:'roomservice.html'}}
    if(a.station==='zineb'){return{section:'Station Zineb',url:'station-zineb.html'}}
    if(a.station==='nour'){return{section:'Station Nour',url:'station-nour.html'}}
    if(a.station==='minorea'){return{section:'Minorea — Capitale',url:'station-minorea.html'}}
    if(a.station==='suyin'){return{section:'Station Suyin',url:'station-suyin.html'}}
    if(a.tag&&!a.station){return{section:'Citoyennes Spéciales',url:'specials.html'}}
    return{section:'Citoyennes expatriées',url:'index.html'};
  }

  function buildMap(all,rs){
    all.forEach(function(a){
      var c=classify(a);
      nameMap[a.name.toLowerCase()]={name:a.name,section:c.section,url:c.url};
    });
    if(rs)rs.forEach(function(a){
      nameMap[a.name.toLowerCase()]={name:a.name,section:'Service de Nuit',url:'roomservice.html'};
    });
    loaded=true;
  }

  Promise.all([
    fetch('data.json').then(function(r){return r.json()}),
    fetch('data-roomservice.json').then(function(r){return r.json()}).catch(function(){return []})
  ]).then(function(results){
    buildMap(results[0],results[1]);
  });

  // Suggestion element
  var suggest=document.createElement('div');
  suggest.id='locate-suggest';
  suggest.style.cssText='display:none;max-width:500px;margin:0 auto 14px;padding:14px 20px;border-radius:12px;background:rgba(232,200,120,0.08);border:1px solid rgba(232,200,120,0.3);text-align:center;font-size:0.9rem;color:#e8c878;backdrop-filter:blur(8px);font-family:inherit';

  function insertSuggest(){
    if(document.getElementById('locate-suggest'))return;
    var sb=document.querySelector('.searchbar,.toolbar,.search-wrap');
    if(sb){sb.parentNode.insertBefore(suggest,sb.nextSibling);return}
    var input=document.getElementById('search');
    if(input&&input.parentNode){input.parentNode.insertBefore(suggest,input.nextSibling);return}
  }

  var debounceTimer;
  function checkSearch(){
    if(!loaded)return;
    var input=document.getElementById('search');
    if(!input)return;
    var q=input.value.trim().toLowerCase();
    if(!q||q.length<2){suggest.style.display='none';return}
    var grid=document.getElementById('grid');
    var hasResults=grid&&grid.children.length>0;
    if(hasResults){suggest.style.display='none';return}
    // No local results — check map
    var match=nameMap[q];
    if(!match){
      var keys=Object.keys(nameMap);
      for(var i=0;i<keys.length;i++){
        if(keys[i].includes(q)){match=nameMap[keys[i]];break}
      }
    }
    if(match){
      insertSuggest();
      suggest.innerHTML='<strong>'+match.name+'</strong> est dans la section <a href="'+match.url+'" style="color:#e8c878;text-decoration:underline;font-weight:500">'+match.section+'</a>';
      suggest.style.display='block';
    }else{
      suggest.style.display='none';
    }
  }

  document.addEventListener('input',function(e){
    if(e.target&&e.target.id==='search'){
      clearTimeout(debounceTimer);
      debounceTimer=setTimeout(checkSearch,400);
    }
  });
  setTimeout(insertSuggest,1000);
})();
