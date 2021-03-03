import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: MyHomePage(title: 'Aula 0'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int on = 1;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
                onPressed: _show,
                child: Text('Clique Aqui',
                    style: TextStyle(fontSize: 15, color: Colors.black))),
            Container(
              margin: EdgeInsets.all(20),
            ),
            Text('Bem vindo ao',
                style: TextStyle(
                    color: on == 0 ? Colors.white : Colors.black,
                    fontSize: 40,
                    fontWeight: FontWeight.bold)),
            Image.asset('logo.jpg'),
          ],
        ),
      ),
    );
  }

  _show() {
    on == 1 ? on = 0 : on =1;
    return;
  }
}
