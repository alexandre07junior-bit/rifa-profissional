<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sorteio Premiado</title>
    <style>
        :root { --primary: #007bff; --success: #28a745; --danger: #dc3545; }
        body { font-family: sans-serif; margin: 0; padding: 10px; background: #f4f4f4; text-align: center; }
        .grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 20px; }
        .number { padding: 15px; background: white; border: 1px solid #ccc; cursor: pointer; border-radius: 8px; font-weight: bold; }
        .number.sold { background: #ccc; cursor: not-allowed; }
        .number.selected { background: var(--primary); color: white; }
        #checkout, #admin-panel { margin-top: 20px; padding: 20px; background: white; border-radius: 10px; display: none; }
        button { padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; margin: 5px; }
        .btn-pix { background: var(--success); color: white; width: 100%; }
        input { width: 90%; padding: 10px; margin: 5px 0; border: 1px solid #ccc; border-radius: 5px; }
    </style>
</head>
<body>

    <h1>Escolha seu Número</h1>
    <div id="grid" class="grid"></div>

    <div id="checkout">
        <h2>Finalizar Compra</h2>
        <input type="text" id="name" placeholder="Nome Completo" required>
        <input type="tel" id="phone" placeholder="WhatsApp (DDD + Número)" required>
        <p>Valor: R$ 5,00</p>
        <button class="btn-pix" onclick="confirmPurchase()">Pagar via Pix</button>
    </div>

    <div id="pix-area" style="display:none; padding: 20px; background: #e9ecef;">
        <p>Chave Pix: <strong>01969189606</strong></p>
        <button onclick="copyPix()">Copiar Chave</button>
    </div>

    <div style="margin-top: 30px;">
        <button onclick="showAdmin()">Acessar ADM</button>
    </div>

    <div id="admin-panel">
        <h3>Painel Administrativo</h3>
        <input type="password" id="admin-pass" placeholder="Senha">
        <button onclick="loginAdmin()">Entrar</button>
        <div id="admin-content" style="display:none;">
            <div id="report"></div>
            <button onclick="startDraw()" style="background: var(--danger); color: white;">Realizar Sorteio</button>
        </div>
    </div>

    <div id="draw-screen" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:white; z-index:1000; padding-top: 20%;">
        <h1 id="draw-number" style="font-size: 100px;">0</h1>
    </div>

    <script>
        let selectedNumber = null;
        let sold = JSON.parse(localStorage.getItem('sold')) || {};

        function renderNumbers() {
            const grid = document.getElementById('grid');
            grid.innerHTML = '';
            for(let i = 1; i <= 100; i++) {
                const div = document.createElement('div');
                div.className = 'number' + (sold[i] ? ' sold' : '');
                div.innerText = i;
                div.onclick = () => { if(!sold[i]) selectNumber(i, div); };
                grid.appendChild(div);
            }
        }

        function selectNumber(num, el) {
            selectedNumber = num;
            document.querySelectorAll('.number').forEach(n => n.classList.remove('selected'));
            el.classList.add('selected');
            document.getElementById('checkout').style.display = 'block';
        }

        function confirmPurchase() {
            const name = document.getElementById('name').value;
            if(!name) return alert('Preencha o nome');
            sold[selectedNumber] = { name, phone: document.getElementById('phone').value };
            localStorage.setItem('sold', JSON.stringify(sold));
            document.getElementById('checkout').style.display = 'none';
            document.getElementById('pix-area').style.display = 'block';
            renderNumbers();
        }

        function copyPix() { navigator.clipboard.writeText('01969189606'); alert('Chave copiada!'); }

        function showAdmin() { document.getElementById('admin-panel').style.display = 'block'; }

        function loginAdmin() {
            if(document.getElementById('admin-pass').value === 'brayan2905') {
                document.getElementById('admin-content').style.display = 'block';
                let report = 'Compradores: <br>';
                for(let n in sold) report += `Número ${n}: ${sold[n].name} <br>`;
                document.getElementById('report').innerHTML = report;
            } else { alert('Senha incorreta'); }
        }

        function startDraw() {
            document.getElementById('draw-screen').style.display = 'block';
            let count = 0;
            const interval = setInterval(() => {
                document.getElementById('draw-number').innerText = Math.floor(Math.random() * 100) + 1;
                count++;
                if(count > 30) {
                    clearInterval(interval);
                    const winner = Math.floor(Math.random() * 100) + 1;
                    document.getElementById('draw-number').innerText = `Ganhador: ${winner} - ${sold[winner]?.name || 'Sem dono'}`;
                }
            }, 1000);
        }

        renderNumbers();
    </script>
</body>
</html>
