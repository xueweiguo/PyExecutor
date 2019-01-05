

import android.app.Activity
import android.app.AlertDialog
import android.app.Dialog
import android.content.DialogInterface
import android.text.Editable
import android.view.View
import android.view.View.OnClickListener
import android.widget.AdapterView.OnItemClickListener
import android.widget.Button
import android.widget.EditText

class DialogCreator {
	Activity activity
	DialogCreator(Activity _activity){
		activity = _activity
	}
	
	AlertDialog createAlertDialog(final int dialog_id, final int msg_id){
		AlertDialog.Builder builder = new AlertDialog.Builder(activity)
		builder.setMessage(activity.getText(msg_id))
		       .setCancelable(false)
		       .setPositiveButton("OK", new DialogInterface.OnClickListener() {
		           void onClick(DialogInterface dialog, int id) {
		        	   activity.removeDialog(dialog_id)
		           }
		       })
		return builder.create()
	}
	
	AlertDialog createAlertDialog(final int dialog_id, CharSequence msg){
		AlertDialog.Builder builder = new AlertDialog.Builder(activity)
		builder.setMessage(msg)
		       .setCancelable(false)
		       .setPositiveButton("OK", new DialogInterface.OnClickListener() {
		           void onClick(DialogInterface dialog, int id) {
		        	   activity.removeDialog(dialog_id)
		           }
		       })
		return builder.create()
	}
	
	AlertDialog createAlertDialog(final int dialog_id, CharSequence[] items, 
    		OnItemClickListener listener){
      	AlertDialog.Builder builder = new AlertDialog.Builder(activity)
    	builder.setTitle(dialog_id)
    	builder.setItems(items, null)
    	builder.setOnCancelListener(new DialogInterface.OnCancelListener() {
    		@Override
			void onCancel(DialogInterface dialog) {
    			activity.removeDialog(dialog_id)
			}
		})
		AlertDialog dialog =  builder.create()
		dialog.getListView().setOnItemClickListener(listener)
		return dialog
    }
	
	private class MyClickListener implements OnClickListener{
		Dialog dialog
		int dialogId
		TextCommand okCmd
		MyClickListener(Dialog dlg, int id, TextCommand cmd){
			dialog = dlg
			dialogId = id
			okCmd = cmd
		}
		//@Override
		void onClick(View v) {
			Editable edit = ((EditText)dialog.findViewById(R.id.inputText)).getText()
			String text = edit.toString()
			okCmd.execute(text)
			activity.removeDialog(dialogId)
		}
	}
	
	Dialog createInputTextDialog(final int id, String original, TextCommand okCmd){
    	final Dialog dialog = new Dialog(activity)

    	dialog.setContentView(R.layout.textdlg)
    	dialog.setTitle(id)
    	EditText et = (EditText)dialog.findViewById(R.id.inputText)
    	if(original != null){
    		et.setText(original)
    	}
    	((Button)dialog.findViewById(R.id.buttonOK)).setOnClickListener(new MyClickListener(dialog, id, okCmd))
		
    	((Button)dialog.findViewById(R.id.buttonCancel)).setOnClickListener(new OnClickListener(){
    		//@Override
    		void onClick(View v) {
    			activity.removeDialog(id)
    		}
    	})
    	
    	return dialog
    }
}
