<?php
function tambah($a, $b){
    return $a + $b;
}

function kurang($x, $y){
    return $x - $y;
}

function kali($p, $q){
    return $p * $q;
}

function bagi($c, $d){
    return $c / $d;
}

function modulus($e, $f){
    return $e % $f;
}

function pangkat($g, $h){
    return $g ** $h;
}

echo "Hasil penjumlahan dari 2 + 2 = ", tambah(2,2);
echo "\nHasil pengurangan dari 3 - 4 = ", kurang(3,4);
echo "\nHasil perkalian dari   6 * 2 = ", kali(6,2);
echo "\nHasil pembagian dari   8 / 4 = ", bagi(8,4);
echo "\nHasil modulus dari     7 % 3 = ", modulus(7,3);
echo "\nHasil pangkat dari    5 ** 4 = ", pangkat(5,4);
?>
