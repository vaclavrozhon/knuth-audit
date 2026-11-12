% Audit-only correction: form the signed displacement before scaling.
@x
  source=shift_right(cur_loc,2,0);
  dest=shift_right(val_stack[1].equiv,2,0);
  acc=ominus(dest,source);
@y
  acc=shift_right(ominus(val_stack[1].equiv,cur_loc),2,0);
@z

@x
  source=shift_right(cur_loc,2,0);
  dest=shift_right(val_stack[0].equiv,2,0);
  acc=ominus(dest,source);
@y
  acc=shift_right(ominus(val_stack[0].equiv,cur_loc),2,0);
@z
