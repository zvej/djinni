// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from parcelable.djinni

package com.dropbox.djinni.test;

import java.util.ArrayList;
import java.util.HashMap;
import javax.annotation.CheckForNull;
import javax.annotation.Nonnull;

public class ParcelableMapList implements android.os.Parcelable {


    /*package*/ final HashMap<String, ArrayList<String>> mMapSet;

    public ParcelableMapList(
            @Nonnull HashMap<String, ArrayList<String>> mapSet) {
        this.mMapSet = mapSet;
    }

    @Nonnull
    public HashMap<String, ArrayList<String>> getMapSet() {
        return mMapSet;
    }

    @Override
    public String toString() {
        return "ParcelableMapList{" +
                "mMapSet=" + mMapSet +
        "}";
    }


    public static final android.os.Parcelable.Creator<ParcelableMapList> CREATOR
        = new android.os.Parcelable.Creator<ParcelableMapList>() {
        @Override
        public ParcelableMapList createFromParcel(android.os.Parcel in) {
            return new ParcelableMapList(in);
        }

        @Override
        public ParcelableMapList[] newArray(int size) {
            return new ParcelableMapList[size];
        }
    };

    public ParcelableMapList(android.os.Parcel in) {
        this.mMapSet = new HashMap<String, ArrayList<String>>();
        in.readMap(this.mMapSet, getClass().getClassLoader());
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(android.os.Parcel out, int flags) {
        out.writeMap(this.mMapSet);
    }

}