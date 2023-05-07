init -99 python:
    def flatten_child(trans, st, at):
        """Flattens the ATL Transform child and sets it."""
        flatten = Flatten(trans.child)
        trans.set_child(flatten)
        return None

    def change_attributes(remove, attr, trans, child=None):
        """
        Add or removes layer attributes to a ImageReference object obtained as the
        ATL Transform child.

        Keyword arguments:
        remove -- If True, it removes attributes to the child, otherwise it adds them.
        attr -- A string or a list of strings which are the names of the attributes to append to the LayeredImage's ImageReference.
        trans -- The ATL Transform object, when the child is not provided, it is retrieved from the transform.
        child -- The child that undergoes the transform, provided by the 'at' clause.

        Notes:
        This appends the attribute directly into the displayable, so no checks are
        done. Also, this is highly experimental.
        """

        if not attr:
            return

        if isinstance(attr, str):
            attr = list([attr])

        try:
            attr[0]
        except:
            raise Exception("Invalid provided attribute to add or remove. Possible input: str, list, RevertableList. Provided:", str(type(attr)))

        if not child:
            child = trans.child

        while not isinstance(child, renpy.display.image.ImageReference):
            try:
                child = child.child
            except:
                raise Exception("Could not add the specified attribute. The provided object final child is not an image.")

        layer_tuple = child.__getattribute__('name')
        layer_list = list(layer_tuple)

        if remove:
            for item in attr:
                if item in layer_list:
                    layer_list.remove(item)
        else:
            for item in attr:
                layer_list = filter_prefix_attrib(item, layer_list)
                if item not in layer_list:
                    layer_list.append(item)

        final_tuple = tuple(layer_list)

        child.__setattr__('name', final_tuple)

        trans.set_child(child)
        trans.update()

        renpy.log(trans)

        return None

    def filter_prefix_attrib(attrib, list):
        """
        Remove layer attributes to a list (The name attribute of an ImageReference)
        if the attribute prefix matches any of the items in the list.

        Keyword arguments:
        attrib -- The attribute to match its prefix.
        list  --  A list of strings which are the names of the attributes of a LayeredImage's ImageReference.
        """
        if isinstance(attrib, str) and attrib.find('_') > 0:
            index = attrib.find('_')
            prefix = attrib[:index]
            for item in list:
                if item[:index] == prefix:
                    list.remove(item)
        return list

    def unc_add_attributes(attr, *args):
        child = None
        trans = None

        for arg in args:
            if isinstance(arg, renpy.display.image.ImageReference):
                child = arg
            if isinstance(arg, renpy.display.transform.ATLTransform):
                trans = arg

        if trans is None:
            raise Exception("Unable to find provided ATL Transform within the provided arguments.")

        change_attributes(False, attr, trans, child)
        return None

    def unc_remove_attributes(attr, *args):
        child = None
        trans = None

        for arg in args:
            if isinstance(arg, renpy.display.image.ImageReference):
                child = arg
            if isinstance(arg, renpy.display.transform.ATLTransform):
                trans = arg

        if trans is None:
            raise Exception("Unable to find provided ATL Transform within the provided arguments.")

        change_attributes(True, attr, trans, child)
        return None

    add_attributes = renpy.curry(unc_add_attributes)
    remove_attributes = renpy.curry(unc_remove_attributes)
