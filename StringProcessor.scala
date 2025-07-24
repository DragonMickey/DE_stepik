/*
Вам дан фрагмент кода, который выполняет операции над списком строк.
Код написан в императивном стиле, использует изменяемые переменные и циклы.
Ваша задача — преобразовать этот код в функциональный стиль.
*/
object StringProcessor {
  def processStrings(strings: List[String]): List[String] = {
    strings.filter(_.length > 3).map(_.toUpperCase) 
    /* Мы используем метод filter, чтобы отобрать слова длиной больше 3.
    Затем метод map, чтобы преобразовать отобранные слова в верхний регистр и сразу же возвращаем полученный результат
     без использования изменяемых переменных и циклов.
    Нижнее подчёркиваение _ означает сокращённую запись дял анонимной функции,
     например _.length > 3 эквивалентно (word: String) => word.length > 3

    var result = List[String]()
    for (str <- strings) {
      if (str.length > 3) {
        result = result :+ str.toUpperCase
      }
    }
    result
*/
  }

  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    val processedStrings = processStrings(strings)
    println(s"Processed strings: $processedStrings")
  }
}
