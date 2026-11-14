// Original, dependency-free SVG silhouettes. All seventeen roles share a classical pedestal; lettered discs remain optional.
export const CODES={p:'P',n:'N',b:'B',r:'R',q:'Q',k:'K',e:'BE',h:'HV',v:'HN',m:'MI',t:'AN',u:'CO',w:'WA',a:'AR',c:'CH',s:'BA',l:'LA'};
const shapes={
p:'<circle cx="30" cy="16" r="7"/><path d="M24 25h12l-3 8 7 12H20l7-12zM17 48h26v5H17z"/>',
r:'<path d="M16 10h7v8h4v-8h6v8h4v-8h7v17l-6 4 1 13H21l1-13-6-4zM16 48h28v5H16z"/><path d="M23 28h14"/>',
n:'<path d="m17 45 5-11 12-7-10-1-7 5-5-6 9-15 5 2 7-5 3 8c12 7 12 17 8 30zM16 48h29v5H16z"/><path d="M24 19h2m9 3c5 6 3 12-2 17" fill="none"/>',
b:'<path d="M30 8c-5 7-13 13-9 21l6 5-5 10h16l-5-10 6-5c4-8-4-14-9-21zM19 48h22l4 5H15z"/><path d="m33 17-7 10" fill="none"/>',
q:'<path d="m15 20 7 23h16l7-23-10 9-5-14-5 14zM20 47h20l5 6H15z"/><circle cx="14" cy="16" r="3"/><circle cx="30" cy="11" r="3"/><circle cx="46" cy="16" r="3"/>',
k:'<path d="M30 5v15m-6-9h12" fill="none" stroke-width="3"/><path d="M30 24c-11-12-21 0-12 10l7 10h10l7-10c9-10-1-22-12-10zM22 48h16l6 5H16z"/>'};
const base='<path d="M22 35h16l-2 8 7 5H17l7-5zM16 49h28v5H16z"/>';
Object.assign(shapes,{
e:base+'<path d="M29 18c-13-14-21 3-7 11l8 5 8-5c14-8 6-25-7-11z"/><ellipse cx="30" cy="24" rx="6" ry="11"/><path d="M25 23h10m-10 6h10M27 13l-4-5m10 5 4-5" fill="none"/>',
h:base+'<path d="M17 33v-6c0-5 4-6 4-10 0-6 18-6 18 0 0 4 4 5 4 10v6z"/><path d="M21 19h18M18 26h24" fill="none"/><path d="M26 34v-5a4 4 0 0 1 8 0v5"/>',
v:base+'<path d="m30 6 4 11 13-4-7 14-10 8-10-8-7-14 13 4z"/><path d="m30 13 0 19m-7-8 7 5 7-5" fill="none"/>',
m:base+'<path d="M20 13q10-7 20 0v13l-10 9-10-9z"/><path d="m24 19 4 2m4 0 4-2m-11 8q5 4 10 0M30 12v20" fill="none"/>',
t:base+'<circle cx="30" cy="11" r="4"/><path d="M30 15v19M20 21h20M15 26q0 12 15 8 15 4 15-8m-30 0 5 2m25-2-5 2" fill="none" stroke-width="3"/>',
u:base+'<path d="M19 18h22v16H19zM23 18v-5h14v5"/><path d="m19 20 11 8 11-8M30 8l7-4" fill="none"/>',
w:base+'<path d="M17 13 30 8l13 5v12q-2 7-13 11-11-4-13-11z"/><path d="M30 13v17m-8-12h16" fill="none"/>',
a:base+'<path d="M30 6c-7 9-13 13-10 21l10 8 10-8c3-8-3-12-10-21z"/><path d="M17 23v10h26V23m-9-8-8 10" fill="none"/>',
c:base+'<path d="M17 10h7v7h5v-7h6v7h7v13l-7 5H24l-7-5z"/><path d="m23 29 5-9 7 2-5 5 6 4" fill="none"/>',
s:base+'<path d="M15 13h8v7h4v-7h6v7h4v-7h8v21H15z"/><path d="M25 34v-9h10v9m-20-8h8m14 0h8" fill="none"/>',
l:base+'<path d="m30 4 6 10-4 5v15h-4V19l-4-5zM20 27h20v5H20z"/><path d="m34 16 8 5-8 3"/>'
});
export function pieceMarkup(p,allTokens=false){const white=p.c==='w',fill=white?'#fffdf5':'#252522',stroke=white?'#30312c':'#11120f';if(shapes[p.t]&&!allTokens)return `<g fill="${fill}" stroke="${stroke}" stroke-width="1.7" stroke-linejoin="round" stroke-linecap="round">${shapes[p.t]}</g>`;return `<circle cx="30" cy="30" r="22" fill="${fill}" stroke="${stroke}" stroke-width="2"/><circle cx="30" cy="30" r="18" fill="none" stroke="${white?'#b6b5a8':'#72736b'}" stroke-width=".8"/><text x="30" y="35" text-anchor="middle" font-family="Georgia,serif" font-weight="bold" font-size="16" fill="${white?'#272821':'#fffdf5'}">${CODES[p.t]}</text>`;}
export const icon=(p,tokens=false)=>`<svg viewBox="0 0 60 60" aria-hidden="true">${pieceMarkup(p,tokens)}</svg>`;
