# Minecraft-Auto-House-Builder

AutoHouseBuilder

インストール手順  
1.RspberryJamMod <https://github.com/arpruss/raspberryjammod/releases>をインストールします  
(この時、インストーラーの画面で"Raspberry Jam Mod","Sample Python scripts and mcpi framework",
 そしてPython3系列の"Python interpreter"にチェックを入れ同時にインストールしてください）
2.一度マインクラフトを起動します  
3.Minecraftディレクトリにmcpipyフォルダが生成されているはずですのでそこにダウンロードしたHouse.pyファイルなどを配置します  

簡易的な紹介動画 → <https://youtu.be/hONcyUKHqMg>  

使い方  
マインクラフトを起動し、/py house 又は /py house100　とコマンドを入力します  

・/py house　の場合、プレイヤーの位置からみて南東方向にランダムに一軒住宅が生成されます  
プレイヤーから見てX軸、Z軸のプラス方向25ブロック以内に金ブロックが置かれているとその金ブロックの位置とプレイヤーのいるブロックの斜め南東方向のブロックを角として住宅が生成されます。  
おおよそ10秒程度で完成します（※PCのスペックに依存すると思われます）  

・/py house100　の場合、金ブロックで住宅の大きさを指定することはできません  
　プレイヤーのブロックから南東方向に住宅が10x10の100軒生成されます。  
　プレイヤーの南東方向200ブロック程度に建造物がないことを確認して実行してください  
　おおよそ15分程度で完成します（※PCのスペックに依存すると思われます）  

・/py HouseR 又は /py HouseR100で回転を前提とした住宅が生成されるようになりました  
  板ガラスや鉄格子の窓がそれぞれフルブロックに置換されるようになりました  
　実際に回転をする場合はWorldEditの//deformコマンドを使用することを推奨します  

・/py stopコマンドで生成を停止できるようになりました  

・どちらのコマンドも生成される場所に空気以外のブロックがあると不具合を起こす可能性がありますので、お気を付けください  

その他  
・バージョンの都合上1.13以降のバージョンには対応していないため、それ以降のバージョンで住宅を使用したい場合はWorldEditなどを用いて1.12.2で生成した住宅をschematic形式でそれ以降のバージョンに移設することを推奨します  
・作者はプログラミングを学び始めて間もないため、不合理なプログラムがあるかもしれません  
・エラーなどが出た場合はGithubや製作者のTwitter<https://twitter.com/craft2424>にて教えてください  
・使用方法がわからない場合なども気軽に連絡してください  
・生成された住宅を使用しTwitterやYoutubeなどに投稿する場合、特に記載はいりませんがご一報いただけれととても喜びます。但し自作発言などはおやめください
・商業的に使用、公開する場合は私に連絡をしてください  
・あまりにも悪質な使用が見られた場合、全体の配布を中止する可能性があります  
・RaspberryJuicePluginでの動作の可否は分かりません。もし使用できた場合はご一報くださるとありがたいです  
・改造などは自由に行って構いませんが、配布する際はご一報ください    
・本プログラムで生じた一切の損害も責任は負いません  
・各種建築サーバーで使用する際はご一報お願いします  
・建築サーバーへの試験に本プログラムで生成した住宅を使用することは厳禁です  
