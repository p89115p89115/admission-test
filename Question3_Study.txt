1. What is Git and why is it used?

Git是一個版本控制系統，用於跟踪計算機文件的更改和協調多人協作。 Git最初由Linux操作系統的創建者Linus Torvalds開發，旨在管理Linux內核的開發。它使用分佈式版本控制系統的方法，可以在本地或遠程存儲庫中管理代碼。

Git的主要用途是管理代碼，特別是協作開發。它可以讓多個人在同一代碼庫上工作，每個人都可以編輯文件，添加新代碼，查看歷史版本，解決代碼衝突等等。 Git還具有強大的分支和合併功能，使得開發人員可以輕鬆地在不同的分支上進行實驗和測試，並將它們合併到主分支中。

另外，Git還提供了許多其他功能，例如存儲庫的備份和還原，撤銷更改，標籤和註釋歷史版本等等。總之，Git是一種強大的工具，可以大大提高軟件開發團隊的效率和協作能力。


2. What is the difference between List, Dictionary, Tuple and Set in Python?

list 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型
list.append
del list[1]

Tuples 

和list同樣以逗號區隔，但是是以 () 符號將所有元素括起來
同樣可存放不同類型資料

Unmodifiable(不可修改的)：這個特性是Tuples(元組)和List(串列)最大的不同，Tuples(元組)中的元素不可修改，只能唯讀

Dictionary 

每一個元素是以鍵(Key)及值(Value)構成，再由 {} 符號將所有元素括起來
鍵(Key)的資料型態通常我們使用String(字串)或Integer(整數)，而值(Value)可以是任何資料型態。
dictionary[key] 會回傳value的值
dictionary.item() 取出來的會是Tuples(元組)，包含了鍵(Key)與值(Value)。

Set

集合不會包含重複的資料
不能透過數字進行索引，只能循環檢查或使用in、not in來存取判斷集合元素
Set最大的特色就是可以做「集合運算」，ex:聯集、交集、差集
不可變集合(frozenset)，Set 但不可改變其內容

In summary, the main differences between List, Dictionary, Tuple, and Set in Python are:

Tuples and frozenset 不可改變其內容, while Dictionary and list and Set 則可變.
Dictionary requires a key-value pair, while List, Tuple and Set do not.
List and Tuple 是有序的(有index), while Dictionary and Set are unordered.
Set does not allow duplicate elements, while List, Dictionary, and Tuple do.

