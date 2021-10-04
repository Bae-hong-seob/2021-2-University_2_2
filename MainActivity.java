package com.bhs.homework1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    TextView textView,textView2; //계산tlr
    EditText editText; //정답입력
    Button btn1, btn3; //입력완료, 종료버튼

    Random ran = new Random();
    int num1 = ran.nextInt(99) + 1;
    int num2 = ran.nextInt(99) + 1;
    int result = 0;
    String[] oper = {"+", "-"};
    int op = ran.nextInt(2);
    String cal = num1 + oper[op] + num2;
    int count= 0, correct = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (op == 0) {
            result = num1 + num2;
        } else {
            result = num1 - num2;
        }

        textView = (TextView) findViewById(R.id.math);

        textView.setText(cal + "=");

        btn1 = (Button) findViewById(R.id.answer); //입력완료 버튼
        editText = (EditText) findViewById(R.id.edit); //정답 view

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String Num = editText.getText().toString();

                if (Num.equals("")) {
                    Toast.makeText(getApplicationContext(), "정답을 입력하세요.", Toast.LENGTH_LONG).show();
                    return;
                }

                if (Integer.parseInt(Num) == result) {
                    Toast.makeText(getApplicationContext(), "정답입니다.", Toast.LENGTH_LONG).show();
                    count++;
                    correct++;
                    //newgame(view);
                    editText.getText().clear();
                }
                else {
                    Toast.makeText(getApplicationContext(), "틀렸습니다. 정답은 " + result, Toast.LENGTH_LONG).show();
                    editText.getText().clear();
                    count++;
                    newgame(view);
                    editText.getText().clear();
                }


            }
        });

        btn3 = (Button) findViewById(R.id.close); //종료버튼

        btn3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                textView2 = (TextView) findViewById(R.id.result);
                textView2.setText(String.valueOf(count) + "번 중에 " + String.valueOf(correct) + "번 성공, 정답률:" + String.valueOf(String.format("%.2f",(double)correct /(double)count * 100)) + "%");
            }
        });

    }
    public void newgame (View view) {
        String[] oper = {"+", "-"};
        Random random = new Random();
        int num1 = random.nextInt(99) + 1;
        int num2 = random.nextInt(99) + 1;
        int op = random.nextInt(2);
        String numStr1 = String.valueOf(num1);
        String numStr2 = String.valueOf(num2);
        String cal = numStr1 + oper[op] + numStr2;
        switch (op) {
            case 0:
                result = num1 + num2;
                break;
            case 1:
                result = num1 - num2;
                break;
        }
        textView.setText(cal + "=");
    }
}