-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 21 Wrz 2019, 19:47
-- Wersja serwera: 10.4.6-MariaDB
-- Wersja PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `ksiazki`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zbior`
--

CREATE TABLE `zbior` (
  `id` int(11) NOT NULL,
  `autor` text COLLATE utf8_polish_ci NOT NULL,
  `tytul` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `zbior`
--

INSERT INTO `zbior` (`id`, `autor`, `tytul`) VALUES
(1, 'Seweryna Szmaglewska', 'Dymy nad Birkenau'),
(2, 'Piotr Cywiński, Władysław Bartoszewski', 'Mój Auschwitz'),
(3, 'Lucyna Gruszczyńska - Jeleńska', 'Ocalona z obozu śmierci'),
(4, 'Aleksandra Wójcik, Maciej Zdziarski', 'Dobranoc Auschwitz'),
(5, 'Wanda Półtawska', 'I boję się snów'),
(6, 'Igor Bartosik', 'Biały domek. Historia Zagłady w bunkrze II'),
(7, 'Józef Seweryn', 'Usługiwałem esesmanom w Auschwitz'),
(8, 'Sylwia Winnik', 'Dziewczęta z Auschwitz'),
(9, 'Leszek Adamczewski', 'W królestwie Hansa Franka'),
(10, 'Adam Willma', 'Ja z krematorium Auschwitz'),
(11, 'Kazimierz Piechowski', 'Byłem numerem. Świadectwa z Auschwitz'),
(12, 'Jerzy Bielecki', 'Kto ratuje jedno życie'),
(13, 'Aleksander Kamiński', 'Kamienie na szaniec'),
(14, 'Anne Frank', 'Dziennik Anne Frank'),
(15, 'Stanisław Sterkowicz', 'Zbrodnicze eksperymenty medyczne w obozach koncentracyjnych III Rzeszy'),
(16, 'Vivien Spitz', 'Doktorzy z piekła rodem'),
(17, 'Ulrich Volklein', 'Josef Mengele. Doktor z Auschwitz'),
(18, 'Nicholas Kulish', 'Doktor śmierć'),
(19, 'Zdzisław Jan Ryn', 'Medycyna za drutami'),
(20, 'Miklos Nyiszli', 'Byłem asystentem doktora Mengele'),
(21, 'John Ware, Gerald Posner', 'Mengele'),
(22, 'Ernst Klee', 'Auschwitz. Medycyna III Rzeszy i jej ofiary'),
(23, 'Laurence Rees', 'Auschwitz. Naziści i ostateczne rozwiązanie'),
(24, 'Kazimierz Tymiński', 'Uspokoić sen'),
(25, 'Stanisław Piotrowski', 'Dziennik Hansa Franka'),
(26, 'Andrej Pogożew', 'Ucieczka z Auschwitz'),
(27, 'Rudolf Hoess', 'Wyznanie spod szubienicy'),
(28, 'Wiktor Krajewski', 'Wiem, jak wygląda piekło');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `zbior`
--
ALTER TABLE `zbior`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `zbior`
--
ALTER TABLE `zbior`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
