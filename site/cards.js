// Adapted from MoveGrid.tsx: actual Standard Pack coordinates, with player rotation.
const data=JSON.parse(document.querySelector('#card-data').textContent);
const buttons=[...document.querySelectorAll('[data-card]')],grid=document.querySelector('#move-grid'),perspective=document.querySelector('#perspective');
let active=0;
function render(){
 const card=data.cards[active],sign=perspective.value==='red'?1:-1;
 buttons.forEach((b,i)=>b.setAttribute('aria-pressed',String(i===active)));
 document.querySelector('#card-name').textContent=card.name[data.lang==='zh'?'zh':'en'];
 grid.dataset.player=perspective.value;
 grid.replaceChildren(...Array.from({length:25},(_,index)=>{
  const cell=document.createElement('span'),r=Math.floor(index/5),c=index%5;
  const center=r===2&&c===2,move=card.moves.some(p=>r===2-sign*p.y&&c===2+sign*p.x);
  cell.className=center?'origin':move?'destination':'';
  cell.setAttribute('aria-hidden','true');return cell;
 }));
 document.querySelector('#move-description').textContent=data.lang==='zh'?`${card.moves.length} 个相对落点。切换视角查看对方方向。`:`${card.moves.length} relative destinations. Switch perspective to see the opposite orientation.`;
}
buttons.forEach((b,i)=>b.addEventListener('click',()=>{active=i;render();}));perspective.addEventListener('change',render);render();
