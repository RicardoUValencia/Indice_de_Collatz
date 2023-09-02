# Análisis de Algoritmos 
## Indice_de_Collatz
<h3> La conjetura o índice de Collatz es sencilla de comprender pero difícil de demostrar ya que menciona que partiendo de cualquier número entero positivo n>0 : </h3>
    <h4> Caso 1: Si n es par lo dividimos entre 2 </h4>
    <h4> Caso 2: Si n es impar multiplicamos por 3 y sumamos 1 </h4>
        <br>
    <h4> Repitiendo secuencialmente estos pasos y siempre llegaremos a 1 </h4>
    
 <h4> Es una función cuyo dominio y codominio son los números naturales </h4>
      <p align="center">
            <img src="https://www.monografias.com/trabajos102/comprobacion-conjetura-collatz/ximage002.jpg.pagespeed.ic.BxEmJdphmP.webp">
      <p>
      
<h4>Ejemplo: 
    Definimos por simplicidad f(n) como c(n) y #c será el resultado que dependerá del valor que tome n y sea evaluado según los casos descritos anteriormente
    <table style="width: 100%; text-align: center;">
        <tr>
          <td style="width: 33%;">n</td>
          <td style="width: 33%;">#C</td>
        </tr>
        <tr>
          <td style="width: 33%;">1</td>
          <td style="width: 33%;">0</td>
        </tr>
        <tr>
          <td style="width: 33%;">2</td>
          <td style="width: 33%;">1</td>
        </tr>
        <tr>
          <td style="width: 33%;">3</td>
          <td style="width: 33%;">7</td>
        </tr>
        <tr>
          <td style="width: 33%;">4</td>
          <td style="width: 33%;">2</td>
        </tr>
        <tr>
          <td style="width: 33%;">5</td>
          <td style="width: 33%;">5</td>
        </tr>
        <tr>
          <td style="width: 33%;">6</td>
          <td style="width: 33%;">8</td>
        </tr>
        <tr>
          <td style="width: 33%;">7</td>
          <td style="width: 33%;">16</td>
        </tr>
        <tr>
          <td style="width: 33%;">8</td>
          <td style="width: 33%;">3</td>
        </tr>
        <tr>
          <td style="width: 33%;">⁞</td>
          <td style="width: 33%;">⁞</td>
        </tr>
    </table>
    
    Resolvemos por ejemplo cuándo n=9, es decir,
    9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
</h4>


         
