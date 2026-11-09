document.addEventListener('DOMContentLoaded',()=>{
 const read=(key,fallback)=>{try{return JSON.parse(localStorage.getItem(key))??fallback}catch{return fallback}};
 const write=(key,value)=>{try{localStorage.setItem(key,JSON.stringify(value))}catch{}};
 document.querySelectorAll('.local-checklist').forEach(list=>{
  const boxes=[...list.querySelectorAll('input[type=checkbox]')],key='labpath-checklist-'+list.id,values=read(key,[]);
  boxes.forEach((b,i)=>{b.checked=values.includes(i);b.addEventListener('change',()=>{write(key,boxes.flatMap((x,j)=>x.checked?[j]:[]));update()})});
  function update(){const n=boxes.filter(b=>b.checked).length;list.querySelector('progress').value=n;list.querySelector('.check-status').textContent=n+' of '+boxes.length+' completed'}
  update();
 });
});
